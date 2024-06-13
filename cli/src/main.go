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
            {
                Name:  "generate",
                Usage: "Generates loader with the options provided",

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
