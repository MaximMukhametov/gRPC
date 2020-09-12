package main

import (
	"context"
	"log"
	"os"
	"time"
	"fmt"
	"bufio"

	"google.golang.org/grpc"
    "google.golang.org/grpc/status"
	pb "../proto"
	epb "google.golang.org/genproto/googleapis/rpc/errdetails"

)

const (
	address = "localhost:50051"
)

func main() {
    scanner := bufio.NewScanner(os.Stdin)
    scanner.Scan()
    if err := scanner.Err(); err != nil {
        fmt.Fprintln(os.Stderr, "reading standard input:", err)
    }

	// Set up a connection to the server.
	conn, err := grpc.Dial(address, grpc.WithInsecure(), grpc.WithBlock())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	c := pb.NewCalculateMultiplicationClient(conn)

	// Contact the server and print out its response.
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	r, err := c.Calculate(ctx, &pb.Request{Array: scanner.Text()})
	if err != nil {
		s := status.Convert(err)
		for _, d := range s.Details() {
			switch info := d.(type) {
			case *epb.BadRequest:
				log.Printf("Bad request: %s,\n %s", info, err)
			default:
				log.Printf("Error: %s,\n %s", info, err)
			}
		}
		os.Exit(1)
	}
	fmt.Printf("%.2f\n", r.GetResult())
}