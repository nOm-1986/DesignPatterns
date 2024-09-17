package main

import (
	"fmt"
	"pizzaFactory/factory"
)

func main() {
	pedido1, err := factory.GetPizzaFactory("Hawaiana")
	pedido2, err := factory.GetPizzaFactory("Peperonie")
	if err != nil {
		panic(err)
	} else {
		fmt.Println(pedido1.GetPizzaInfo())
		fmt.Println()
		fmt.Println(pedido2.GetPizzaInfo())
	}

}
