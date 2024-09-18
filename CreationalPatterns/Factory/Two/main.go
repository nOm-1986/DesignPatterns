package main

import (
	ft "factoryGun/types"
	"fmt"
)

func main() {
	ak47, _ := ft.GetGun("ak47")
	mus, _ := ft.GetGun("musket")

	printDetails(ak47)
	printDetails(mus)
}

func printDetails(g ft.IGun) {
	fmt.Printf("Gun: %s", g.GetName())
	fmt.Println()
	fmt.Printf("Power: %d", g.GetPower())
	fmt.Println()
}
