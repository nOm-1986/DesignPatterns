package types

type Table struct {
	tipo string
	size string
	legs int8
}

func (t *Table) GetType() string {
	return t.tipo
}

func (t *Table) GetSize() string {
	return t.size
}

func (t *Table) HasLegs() int8 {
	return t.legs
}
