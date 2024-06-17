package main

import (
        "fmt"
        "os"

        "github.com/urfave/cli/v2"
)

func main() {
    app := &cli.App{
        Name: "MultLdr CLI client",

        Commands: []*cli.Command{
            {
                Name:  "plugs",
                Usage: "Retrieve list of plugins present",

                Flags: []cli.Flag{
                    &cli.StringFlag{
                        Name:        "server",
                        Aliases:     []string{"s"},
                        Value:       "127.0.0.1",
                        Usage:       "Use provided `IP` for the MultLdr server",
                        DefaultText: "127.0.0.1",
                    },
                    &cli.IntFlag{
                        Name:        "port",
                        Aliases:     []string{"p"},
                        Value:       5000,
                        Usage:       "Use provided `PORT` for the MultLdr server",
                        DefaultText: "5000",
                    },
                },
                Action: func(ctx *cli.Context) error {
                    plugins, err  := getPlugins(ctx.String("server"), ctx.Int("port"))

                    if err != nil {
                        fmt.Printf("[!] %v\n", err)
                        return nil
                    }

                    displayPlugins(plugins)

                    return nil
                },
            },
            {
                Name:  "gen",
                Usage: "Generates loader with the options provided",

                Flags: []cli.Flag{
                    &cli.StringFlag{
                        Name:        "server",
                        Aliases:     []string{"s"},
                        Value:       "127.0.0.1",
                        Usage:       "Use provided `IP` for the MultLdr server",
                        DefaultText: "127.0.0.1",
                    },
                    &cli.IntFlag{
                        Name:        "port",
                        Aliases:     []string{"p"},
                        Value:       5000,
                        Usage:       "Use provided `PORT` for the MultLdr server",
                        DefaultText: "5000",
                    },
                    &cli.StringFlag{
                        Name:        "config",
                        Aliases:     []string{"c"},
                        Usage:       "Load configuration from `FILE`",
                    },
                    &cli.StringFlag{
                        Name:        "bin",
                        Aliases:     []string{"b"},
                        Usage:       "Use payload binary from `FILE`",
                        Required:    true,
                    },
                },
                Action: func(ctx *cli.Context) error {
					var config map[string][]string
                    var err error
					if ctx.String("config") != "" {
						config, err = readConfig(ctx.String("config"))
                        if err != nil {
                            fmt.Printf("[!] %v\n", err)
                            return nil
                        }

					} else {
						config = getConfig(ctx.String("server"), ctx.Int("port"))
					}
                    fmt.Printf("[*] Using the following settings:\n")
                    fmt.Printf("\t[>] Keying: %s\n", config["keying"])
                    fmt.Printf("\t[>] Payload mods: %s\n", config["payload_mods"])
                    fmt.Printf("\t[>] Execution: %s\n", config["execution"])
                    fmt.Printf("\t[>] Pre Compilation: %s\n", config["pre_comp"])
                    fmt.Printf("\t[>] Post Compilation: %s\n", config["post_comp"])

					payloadFile := ctx.String("bin")
					fmt.Printf("[*] Using payload file: %s\n", payloadFile)
                    
                    return nil
                },
            },
        },
    }

    if err := app.Run(os.Args); err != nil {
        fmt.Println(err)
    }
}
