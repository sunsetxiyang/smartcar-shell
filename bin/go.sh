#!/bin/bash

gpio_path=/usr/local/bin

#right wheel
$gpio_path/gpio write 6 $1
$gpio_path/gpio write 0 $2

#left wheel
$gpio_path/gpio write 4 $3
$gpio_path/gpio write 5 $4
