package automotive

import "fmt"

type Car struct {
	brand       string
	isPoweredOn bool
	gasCapacity int
}

func NewCar(brand string, gasCapacity int) (*Car, error) {
	return &Car{
		brand:       brand,
		gasCapacity: gasCapacity,
		isPoweredOn: false,
	}, nil
}

func (c *Car) IsPoweredOn() bool {
	return c.isPoweredOn
}

func (c *Car) PowerOn() {
	c.isPoweredOn = true
}

func (c *Car) PowerOff() {
	c.isPoweredOn = false
}

func (c *Car) Honk() {
	fmt.Println("Beep beep!")
}
