/*
block comment.
k250108: first attempt at using go. statically
    typed compiled lanaguage, seems easy to use

mini notes:
    "go run myfile.go" >> developer compile & run, for testing
    "go build myfile.go" >> actually create a binary to use

main questions:
  matrix package?
  plotting?
  gui?
  multithreading / multiprocessing?
  web capabilities (+mqtt?)

*/

package main // line comment: 'package' = collection of one/multiple go files

import "fmt" // specific features of a particular package
import "math"
var print = fmt.Println

func main() {
    //fmt.Println("hey world")
    print("hi")
    print(math.Cos(1))
    


}
