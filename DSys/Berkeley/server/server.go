package main

import (
	"fmt"
	"net"
	"os"
	"strconv"
	"strings"
	"time"

	"berkeley/connect"
)

var client_times []int
var cv_array []int

func Server() {
	server, err := net.Listen(connect.SERVER_TYPE, connect.SERVER_HOST+":"+connect.SERVER_PORT)
	if err != nil {
		fmt.Println("[Time Server] Error listening:", err.Error())
		os.Exit(1)
	}
	defer server.Close()
	fmt.Println("[Time Server] Listening on " + connect.SERVER_HOST + ":" + connect.SERVER_PORT)
	fmt.Println("[Time Server] Waiting for client...")
	for {
		connection, err := server.Accept()
		if err != nil {
			fmt.Println("[Time Server] Error accepting: ", err.Error())
			continue
		}
		fmt.Println("[Time Server] Connected~ ")
		go process_client(connection)
	}
}

func process_client(connection net.Conn) {
	defer connection.Close()
	buffer := make([]byte, 1024)
	var server_time, cv, client_time int
	server_time = int(time.Now().Unix())
	fmt.Println(server_time)

	for ix := 0; ix < connect.NUM_CLIENTS; ix++ {
		mLen, err := connection.Read(buffer)
		if err != nil {
			fmt.Println("[Time Server] Error reading: ", err.Error())
			return
		}
		message := strings.TrimSpace(string(buffer[:mLen]))
		fmt.Println("[Time Server] Received time from client :=", message)
		client_time, _ = strconv.Atoi(message)
		client_times = append(client_times, client_time)
		cv = client_time - server_time
		cv_array = append(cv_array, cv)
		if ix == connect.NUM_CLIENTS-1 {
			new_cv_array := calc_average(cv_array)
			adjusted_server_time := float64(server_time) + new_cv_array[connect.NUM_CLIENTS-1]
			fmt.Printf("Adjusted Server Time: %f\n", adjusted_server_time)
			var new_cv_array_str []string
			for _, val := range new_cv_array[:len(new_cv_array)-1] {
				new_cv_array_str = append(new_cv_array_str, strconv.FormatFloat(val, 'f', -1, 64))
			}
			response := strings.Join(new_cv_array_str, ",")
			_, err = connection.Write([]byte(response))
			if err != nil {
				fmt.Println("[Time Server] Error writing: ", err.Error())
				return
			}
		} else {
			_, err = connection.Write([]byte("ACK"))
			if err != nil {
				fmt.Println("[Time Server] Error writing: ", err.Error())
				return
			}
		}
	}
	client_times = []int{}
	cv_array = []int{}
}

func calc_average(cv_array []int) []float64 {
	var sum int
	var new_cv_array []float64

	all_times := append(cv_array, 0)
	for _, cv := range all_times {
		sum += cv
	}
	caf := float64(sum) / float64(len(all_times))
	fmt.Println("CAF: ", caf)
	for _, cv := range all_times {
		new_cv := caf - float64(cv)
		new_cv_array = append(new_cv_array, new_cv)
	}
	fmt.Println(new_cv_array)
	return new_cv_array
}

func main() {
	Server()
}
