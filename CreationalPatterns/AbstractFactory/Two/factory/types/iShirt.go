package types

type IShirt interface {
	setLogo(logo string)
	setSize(size string)
	GetLogo() string
	GetSize() string
}

type Shirt struct {
	logo string
	size string
}

func (s *Shirt) setLogo(logo string) {
	s.logo = logo
}

func (s *Shirt) GetLogo() string {
	return s.logo
}

func (s *Shirt) setSize(size string) {
	s.size = size
}

func (s *Shirt) GetSize() string {
	return s.size
}
