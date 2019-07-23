package main

import (
	"fmt"
	"bytes"
	"bufio"
	"os"
)

func main() {

	// Using this instead of Scanln since, Scanln breaks at whitespace
	scanner := bufio.NewScanner(os.Stdin)

	// Declaring variables
	var key int
	var message string

	// Usng bytes.Buffer, since more efficinet for concatenation
	var encodedMessage bytes.Buffer
	var decodedMessage bytes.Buffer

	// Taking input
	fmt.Println("Enter key value to use for encryption-")
	fmt.Scanln(&key)
	fmt.Println("Enter the message to send")
	// Since need whitespaces as well
	scanner.Scan()
	message = scanner.Text()

	// Calculating encoded string
	for _,val := range message {
		encodedMessage.WriteString(string(int(val)+key))
	}

	// Printing encoded message
	fmt.Println("Encoded message is-")
	fmt.Println(encodedMessage.String())

	// Calculate decoded message
	for _,val := range encodedMessage.String() {
		decodedMessage.WriteString(string(int(val) - key))
	}

	// Printing decoded message
	fmt.Println("Decoded message is-")
	fmt.Println(decodedMessage.String())
}