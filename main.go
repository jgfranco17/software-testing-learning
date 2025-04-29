package main

import (
	"github.com/jgfranco17/software-testing-learning/automotive"
	"github.com/jgfranco17/software-testing-learning/logging"
	"github.com/sirupsen/logrus"
)

func main() {
	logger := logging.NewLogger(logrus.DebugLevel)
	car, err := automotive.NewCar("Toyota", 100)
	if err != nil {
		logger.Fatalf("Failed to create new car: %v", err)
	}
	logger.Info("New car created")
	car.Honk()
}
