package main

import (
	"context"
	"log"
	"os"
	"time"
	"fmt"
	"bufio"

	"google.golang.org/grpc"
	pb "../proto"
)

const (
	address     = "localhost:50051"
)

func main() {
    // read array of numbers from stdin
    reader := bufio.NewReader(os.Stdin)
    char, err := reader.ReadString('\n')
    if err != nil {
      fmt.Println(err)
    }

    // print out the unicode value i.e. A -> 65, a -> 97
    fmt.Println(char)

	// Set up a connection to the server.
	conn, err := grpc.Dial(address, grpc.WithInsecure(), grpc.WithBlock())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	c := pb.NewGreeterClient(conn)

	// Contact the server and print out its response.
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()
	r, err := c.SayHello(ctx, &pb.HelloRequest{Name: char})
	if err != nil {
		log.Fatalf("could not greet: %v", err)
	}
	log.Printf("Greeting: %s", r.GetMessage())
}