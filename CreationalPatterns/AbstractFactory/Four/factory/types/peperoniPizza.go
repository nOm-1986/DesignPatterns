package types

type PeperoniPizza struct {
	ingredients []string
}

func (PeperoniPizza) PizzaType() string {
	return "🍕 Peperonie 🍕"
}

func (p PeperoniPizza) PizzaIngredients() string {
	ingredientes := ""
	p.setIngredients()
	for _, v := range p.ingredients {
		ingredientes += " " + v + ","
	}
	return "Los ingredientes son: " + ingredientes
}

func (PeperoniPizza) BakingPizza() string {
	return "Horneada por 17 min a 280 grados centigrados"
}

func (PeperoniPizza) CutingPizza() string {
	return "Cortada en 6 porciones"
}

func (h PeperoniPizza) GetPizzaInfo() string {
	info := "Pizza " + h.PizzaType() + ".\n" + h.PizzaIngredients() + ".\n" + h.BakingPizza() + ".\n" + h.CutingPizza() + "."
	return info
}

func (h *PeperoniPizza) setIngredients() {
	h.ingredients = append(h.ingredients, "pizza dough", "tomato paste", "peperonie", "ham", "chese")
}
