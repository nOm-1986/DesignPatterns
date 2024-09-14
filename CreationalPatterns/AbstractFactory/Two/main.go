package main

import (
	"abstractfactory/factory"
)

func main() {
	adidasFactory, _ := factory.GetSportsFactory("adidas")

	adidasShoe := adidasFactory.MakeShoe(40)
	adidasShirt := adidasFactory.MakeShirt("M")

	factory.PrintShoeDetails(adidasShoe)
	factory.PrintShirtDetails(adidasShirt)
}
