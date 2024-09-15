package main

import (
	"fmt"
	"furniturefactory/factory"
)

func main() {
	modernFactory, err := factory.GetFurnitureFactory("moderna")

	if err != nil {
		fmt.Println(err)
	} else {
		moderChair := modernFactory.MakeChair()
		moderSofa := modernFactory.MakeSofa()
		moderTable := modernFactory.MakeTable()

		factory.PrintChairDetails(moderChair)
		factory.PrintSofaDetails(moderSofa)
		factory.PrintTableDetails(moderTable)
		fmt.Println("+++++++++++++++++++++++++++++++++++")
	}

	decoFactory, err := factory.GetFurnitureFactory("artdeco")
	if err != nil {
		fmt.Println(err)
	} else {
		decoChair := decoFactory.MakeChair()
		decoSofa := decoFactory.MakeSofa()
		decoTable := decoFactory.MakeTable()

		factory.PrintChairDetails(decoChair)
		factory.PrintSofaDetails(decoSofa)
		factory.PrintTableDetails(decoTable)
		fmt.Println("+++++++++++++++++++++++++++++++++++")
	}

	victorianaFactory, err := factory.GetFurnitureFactory("victorian")
	if err != nil {
		fmt.Println(err)
	} else {
		vicChair := victorianaFactory.MakeChair()
		vicSofa := victorianaFactory.MakeSofa()
		vicTable := victorianaFactory.MakeTable()

		factory.PrintChairDetails(vicChair)
		factory.PrintSofaDetails(vicSofa)
		factory.PrintTableDetails(vicTable)
		fmt.Println("+++++++++++++++++++++++++++++++++++")
	}
}
