package automotive

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCarInit(t *testing.T) {
	car, err := NewCar("Toyota", 100)
	assert.NoError(t, err, "Unexpected error while creating new car")
	assert.False(t, car.IsPoweredOn())
}

func TestCarPowerCycling(t *testing.T) {
	car, err := NewCar("Toyota", 100)
	assert.NoError(t, err, "Unexpected error while creating new car")
	car.PowerOn()
	assert.True(t, car.IsPoweredOn())
	car.PowerOff()
	assert.False(t, car.IsPoweredOn())
}
