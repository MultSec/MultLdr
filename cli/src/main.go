package main

import (
    "encoding/json"
    "fmt"
    "io/ioutil"
    "net/http"
    "os"

    "github.com/urfave/cli/v2"
)

// Define a struct for the known parts of the JSON structure
type KnownParts struct {
    Execution   map[string][]string `json:"execution"`
    Keying      map[string][]string `json:"keying"`
    PayloadMods map[string][]string `json:"payload_mods"`
    PostComp    map[string][]string `json:"post_comp"`
}

// Function to get plugins from the server
func getPlugins(ip string, port int) {
    fmt.Println("[*] Server IP: ", ip)
    fmt.Println("[*] Server Port: ", port)

    url := fmt.Sprintf("http://%s:%d/api/v1/plugins", ip, port)
    resp, err := http.Get(url)
    if err != nil {
        fmt.Printf("[!] Failed to fetch plugins: %v\n", err)
        return
    }
    defer resp.Body.Close()

    if resp.StatusCode != http.StatusOK {
        fmt.Printf("[!] Server returned non-200 status: %d %s\n", resp.StatusCode, resp.Status)
        return
    }

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Printf("[!] Failed to read response body: %v\n", err)
        return
    }

    var knownParts KnownParts
    if err := json.Unmarshal(body, &knownParts); err != nil {
        fmt.Printf("[!] Failed to parse known parts of JSON: %v\n", err)
        return
    }

    // Parse the unknown parts dynamically
    var dynamicParts map[string]interface{}
    if err := json.Unmarshal(body, &dynamicParts); err != nil {
        fmt.Printf("[!] Failed to parse dynamic parts of JSON: %v\n", err)
        return
    }

    // Remove known parts from the dynamic map
    delete(dynamicParts, "execution")
    delete(dynamicParts, "keying")
    delete(dynamicParts, "payload_mods")
    delete(dynamicParts, "post_comp")

    // Display the known parts
    fmt.Println("[i] Known Plugins retrieved from server:")
    displayPlugins("Execution", knownParts.Execution)
    displayPlugins("Keying", knownParts.Keying)
    displayPlugins("Payload Mods", knownParts.PayloadMods)
    displayPlugins("Post Compilation", knownParts.PostComp)

    // Display the dynamic parts
    if len(dynamicParts) > 0 {
        fmt.Println("[i] Dynamic Plugins retrieved from server:")
        for key, value := range dynamicParts {
            fmt.Printf("\t- %s: %v\n", key, value)
        }
    }
}

// Function to display plugins in a readable format
func displayPlugins(section string, plugins map[string][]string) {
    fmt.Printf("\t- %s:\n", section)
    for key, elements := range plugins {
        fmt.Printf("\t\t- %s:\n", key)
        for _, element := range elements {
            fmt.Printf("\t\t\t- %s\n", element)
        }
    }
}

func main() {
    app := &cli.App{
        Name: "MultLdr CLI client",

        Commands: []*cli.Command{
            {
                Name:  "plugins",
                Usage: "Retrieve list of plugins present",

                Flags: []cli.Flag{
                    &cli.StringFlag{
                        Name:        "server",
                        Aliases:     []string{"s"},
                        Value:       "127.0.0.1",
                        Usage:       "IP for the MultLdr server",
                        DefaultText: "127.0.0.1",
                    },
                    &cli.IntFlag{
                        Name:        "port",
                        Aliases:     []string{"p"},
                        Value:       5000,
                        Usage:       "Port for the MultLdr server",
                        DefaultText: "5000",
                    },
                },
                Action: func(ctx *cli.Context) error {
                    getPlugins(ctx.String("server"), ctx.Int("port"))
                    return nil
                },
            },
        },
    }

    if err := app.Run(os.Args); err != nil {
        fmt.Println(err)
    }
}
