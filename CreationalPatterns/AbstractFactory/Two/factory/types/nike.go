package types

type Nike struct{}

func (n *Nike) MakeShoe(talla int) IShoe {
	return &NikeShoe{
		Shoe: Shoe{
			logo: "Nike",
			size: talla,
		},
	}
}

func (n *Nike) MakeShirt(algo string) IShirt {
	return &NikeShirt{
		Shirt: Shirt{
			logo: "Nike",
			size: algo,
		},
	}
}
