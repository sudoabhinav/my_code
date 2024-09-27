"""
To start the application below steps were followed :-
   - create basic-fiber-application directory
   - run go mod init package_name command, in this case we ran the below command
        -> go mod init basic-fiber-application
   - create main.go with the contents in this file
   - run the below command to install fiber package
        -> go get github.com/gofiber/fiver/v2
   - start the application using the below command
        -> go run main.go
   - application is started at port 3000 and below curl request can be used to check the application response at route "/"
        -> curl --location 'http://127.0.0.1:3000/'

"""
package main

import "github.com/gofiber/fiber/v2"

func main() {
	app := fiber.New()

	app.Get("/", func(c *fiber.Ctx) error {
		return c.SendString("Hello, World!")
	})

	app.Listen(":3000")
}
