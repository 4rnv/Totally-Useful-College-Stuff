package main

// https://medium.com/@viktordev/socket-programming-in-go-write-a-simple-tcp-client-server-c9609edf3671
// https://www.developer.com/languages/intro-socket-programming-go/

import (
	"fmt"
	"net"
	"os"
	"strings"
)

func Server() {
	fmt.Println("server")
	server, err := net.Listen(SERVER_TYPE, SERVER_HOST+":"+SERVER_PORT)
	if err != nil {
		fmt.Println("[Server] Error listening:", err.Error())
		os.Exit(1)
	}
	defer server.Close()
	fmt.Println("[Server] Listening on " + SERVER_HOST + ":" + SERVER_PORT)
	fmt.Println("[Server] Waiting for client...")
	for {
		connection, err := server.Accept()
		if err != nil {
			fmt.Println("[Server] Error accepting: ", err.Error())
			os.Exit(1)
		}
		fmt.Println("[Server] Connected~ ")
		go process_client(connection)
	}
}

func process_client(connection net.Conn) {
	buffer := make([]byte, 1024)
	mLen, err := connection.Read(buffer)
	if err != nil {
		fmt.Println("[Server] Error reading: ", err.Error())
	}
	message := strings.TrimSpace(string(buffer[:mLen]))
	fmt.Println("[Server] Received message from client :=", message)
	length := len(message)
	response := fmt.Sprintf("The length of your message was %d bits", length)
	_, err = connection.Write([]byte(response))
	connection.Close()
}
