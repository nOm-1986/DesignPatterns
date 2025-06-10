package main

import (
	"errors"
	"fmt"
)

type IProduct interface {
	setStock(stock int)
	getStock() int
	setName(name string)
	getName() string
}

type Computer struct {
	name  string
	stock int
}

func (c *Computer) setStock(stock int) {
	c.stock = stock
}

func (c *Computer) setName(name string) {
	c.name = name
}

func (c Computer) getName() string {
	return c.name
}

func (c Computer) getStock() int {
	return c.stock
}

type Laptop struct {
	Computer
}

type Desktop struct {
	Computer
}

func newLapto() IProduct {
	return &Laptop{
		Computer: Computer{
			name:  "Laptop Computer",
			stock: 25,
		},
	}
}

func newDescktop() IProduct {
	return &Desktop{
		Computer: Computer{
			name:  "Desktop Computer",
			stock: 25,
		},
	}
}

// Creational Factory
func GetComputerFactory(computerType string) (IProduct, error) {
	switch computerType {
	case "laptop":
		return newLapto(), nil
	case "desktop":
		return newDescktop(), nil
	default:
		return nil, errors.New("unknow option")
	}
}

func printNameAndStock(p IProduct) {
	fmt.Printf("Product name: %s, with stock %d\n", p.getName(), p.getStock())
}

func main() {
	//lapto, err := GetComputerFactory("laptop")
	desktop, err := GetComputerFactory("desktop")
	if err != nil {
		fmt.Println(err.Error())
	} else {
		//printNameAndStock(lapto)
		printNameAndStock(desktop)
	}
}
