package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"

    "github.com/AlecAivazis/survey/v2"
)

// Define a struct for the known parts of the JSON structure
type Plugins struct {
	PreComp     map[string][]string `json:"pre_comp"`
	Execution   map[string][]string `json:"execution"`
	Keying      map[string][]string `json:"keying"`
	PayloadMods map[string][]string `json:"payload_mods"`
	PostComp    map[string][]string `json:"post_comp"`
}

// Function to get plugins from the server
func getPlugins(ip string, port int) (Plugins, error) {
	var plugins Plugins
	fmt.Println("[*] Server IP: ", ip)
	fmt.Println("[*] Server Port: ", port)

	url := fmt.Sprintf("http://%s:%d/api/v1/plugins", ip, port)
	resp, err := http.Get(url)
	if err != nil {
		return plugins, fmt.Errorf("failed to fetch plugins: %v", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return plugins, fmt.Errorf("server returned non-200 status: %d %s", resp.StatusCode, resp.Status)
	}

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return plugins, fmt.Errorf("failed to read response body: %v", err)
	}

	if err := json.Unmarshal(body, &plugins); err != nil {
		return plugins, fmt.Errorf("failed to parse known parts of JSON: %v", err)
	}

	return plugins, nil
}

func printPlugins(label string, plugins map[string][]string) {
	fmt.Printf("\t[+] %s:\n", label)

	for key, elements := range plugins {
		fmt.Printf("\t\t[-] %s:\n", key)
		for _, element := range elements {
			fmt.Printf("\t\t\t[>] %s\n", element)
		}
	}
}

// Function to display plugins in a readable format
func displayPlugins(plugins Plugins) {
	// Display the known parts
	fmt.Println("[i] Known Plugins retrieved from server:")
	printPlugins("Keying", plugins.Keying)
	printPlugins("Payload Mods", plugins.PayloadMods)
	printPlugins("Execution", plugins.Execution)
	printPlugins("Pre Compilation", plugins.PreComp)
	printPlugins("Post Compilation", plugins.PostComp)
}

// Retrieve config from file
func readConfig(config string) (map[string][]string, error) {
	file, err := os.Open(config)
	if err != nil {
		return nil, fmt.Errorf("failed to open config file: %v", err)
	}
	defer file.Close()

	var conf map[string][]string
	decoder := json.NewDecoder(file)
	if err := decoder.Decode(&conf); err != nil {
		return nil, fmt.Errorf("failed to parse config file: %v", err)
	}

	return conf, nil
}

func Checkboxes(label string, opts []string, oneOption bool) []string {
    res := []string{}
    prompt := &survey.MultiSelect{
        Message: label,
        Options: opts,
    }
	if(oneOption) {
		survey.AskOne(prompt, &res, 
			survey.WithValidator(survey.Required), 
			survey.WithValidator(survey.MinItems(1)), 
			survey.WithValidator(survey.MaxItems(1)), 
			survey.WithRemoveSelectAll(), 
			survey.WithRemoveSelectNone())
	} else {
    	survey.AskOne(prompt, &res, 
			survey.WithRemoveSelectAll(), 
			survey.WithRemoveSelectNone())
	}
    return res
}

// Present menu and retrieve paths for plugins from sections
func getOptions(prefix string, plugins map[string][]string, label string, oneOption bool) []string {
	var options []string

	// Get options
	for key, elements := range plugins {
		for _, element := range elements {
			plugin := "/" + prefix + "/" + key + "/" + element
			options = append(options, plugin)
		}
	}

	return Checkboxes(label, options, oneOption)
}

// Ask user for configuration
func getConfig(ip string, port int) (map[string][]string, error) {
	userConfig := make(map[string][]string)

	plugins, err := getPlugins(ip, port)
	if err != nil {
		return userConfig, err
	}

	fmt.Println("[i] Plugins Selection:")
	userConfig["keying"] 		= getOptions("keying", plugins.Keying, "Keying", false)
	userConfig["payload_mods"] 	= getOptions("payload_mods", plugins.PayloadMods, "Payload Mods", false)
	userConfig["execution"] 	= getOptions("execution", plugins.Execution, "Execution", true)
	userConfig["pre_comp"] 		= getOptions("pre_comp", plugins.PreComp, "Pre Compilation", false)
	userConfig["post_comp"] 	= getOptions("post_comp", plugins.PostComp, "Post Compilation", false)

	return userConfig, nil
}

// Save configuration file
func saveConfigFile(config map[string][]string) {
	fmt.Printf("[?] Save config to file [y/n]? ")

	var saveFile rune
	_, err := fmt.Scanf("%c", &saveFile)
	if err != nil {
		fmt.Printf("[!] %v\n", err)
	}

	if (saveFile == 'y') {
		saveConfigFile(config)
	}

	jsonData, err := json.MarshalIndent(config, "", "    ")
    if err != nil {
        fmt.Printf("\t[!] %v\n", err)
    }

    err = os.WriteFile("config.json", jsonData, 0644)
    if err != nil {
        fmt.Printf("\t[!] %v\n", err)
    }

    fmt.Println("\t[*] Configuration file successfully written to config.json")
}