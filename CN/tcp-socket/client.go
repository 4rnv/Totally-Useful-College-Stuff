package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
)

const (
	SERVER_HOST = "localhost"
	SERVER_PORT = "20000"
	SERVER_TYPE = "tcp"
)

func Client() {
	fmt.Println("client")
	connection, err := net.Dial(SERVER_TYPE, SERVER_HOST+":"+SERVER_PORT)
	if err != nil {
		panic(err)
	}

	var user_message string
	reader := bufio.NewReader(os.Stdin)
	fmt.Println("[Client] Enter your message: ")
	user_message, _ = reader.ReadString('\n')
	_, err = connection.Write([]byte(user_message))

	buffer := make([]byte, 1024)
	mLen, err := connection.Read(buffer)
	if err != nil {
		fmt.Println("[Client] Error reading: ", err.Error())
	}
	fmt.Println("[Client] Received response from server := ", string(buffer[:mLen]))
	defer connection.Close()
}
