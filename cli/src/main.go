package main

import (
    "fmt"
    "log"
    "os"

    "github.com/urfave/cli/v2"
)

func main() {
    app := &cli.App{
        Flags: []cli.Flag{
            &cli.StringFlag{
                Name:  "server",
				Aliases: []string{"s"},
                Value: "127.0.0.1",
                Usage: "IP for the MultLdr server",
				DefaultText: "127.0.0.1",
            },
        },
		Action: func(ctx *cli.Context) error {
			fmt.Println("Server IP: ", ctx.String("server"))
			
			return nil
		},
    }

    if err := app.Run(os.Args); err != nil {
        log.Fatal(err)
    }
}