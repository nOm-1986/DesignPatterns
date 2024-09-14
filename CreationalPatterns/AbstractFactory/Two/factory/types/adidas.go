package types

type Adidas struct {
}

func (a *Adidas) MakeShoe(size int) IShoe {
	return &AdidasShoe{
		Shoe: Shoe{
			logo: "adidas",
			size: size,
		},
	}
}

func (a *Adidas) MakeShirt(talla string) IShirt {
	return &AdidasShirt{
		Shirt: Shirt{
			logo: "adidas",
			size: talla,
		},
	}
}
