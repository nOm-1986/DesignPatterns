package types

type Chair struct {
	tipo string
	size string
	legs int8
}

func (c *Chair) GetType() string {
	return c.tipo
}

func (c *Chair) GetSize() string {
	return c.size
}

func (c *Chair) HasLegs() int8 {
	return c.legs
}
