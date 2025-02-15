package main

import (
	"fmt"
	"math/rand/v2"
	"net"
	"strconv"
	"strings"
	"time"

	"berkeley/connect"
)

func Client() {
	connection, err := net.Dial(connect.SERVER_TYPE, connect.SERVER_HOST+":"+connect.SERVER_PORT)
	if err != nil {
		panic(err)
	}
	defer connection.Close()
	var now, random, client_time int
	var adjustments_str string
	var client_times []int
	now = int(time.Now().Unix())
	for ix := 0; ix < connect.NUM_CLIENTS; ix++ {
		random = (rand.IntN(2001)) - 1000
		client_time = now + random
		fmt.Printf("[Client%d] Random number is: %d\n", ix, random)
		fmt.Printf("Client%d Time is: %d\n", ix, client_time)
		client_times = append(client_times, client_time)
		_, err = connection.Write([]byte(strconv.Itoa(client_time)))
		if err != nil {
			fmt.Printf("[Client%d] Something went wrong\n", ix)
		}
		buffer := make([]byte, 1024)
		mLen, err := connection.Read(buffer)
		if err != nil {
			fmt.Printf("[Client%d] Error reading: %v\n", ix, err.Error())
		}
		if ix == connect.NUM_CLIENTS-1 {
			adjustments_str = string(buffer[:mLen])
			fmt.Printf("[Client%d] Received adjustments: %v \n", ix, adjustments_str)
		}
	}
	adjustments := strings.Split(adjustments_str, ",")
	fmt.Println(adjustments)
	var adjusted_client_times [connect.NUM_CLIENTS]float64
	for i, adjustment := range adjustments {
		adjustment, _ := strconv.ParseFloat(adjustment, 64)
		adjusted_client_times[i] = float64(client_times[i]) + adjustment
		fmt.Printf("New time for client%d is: %f\n", i, adjusted_client_times[i])
	}
	// adjusted_time := float64(client_time) + adjustment
	// fmt.Printf("[Client] Adjusted time: %v\n", adjusted_time)
}

func main() {
	Client()
}
