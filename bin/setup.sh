#!/bin/bash

#set mode

gpio_path=/usr/local/bin

#right wheel
$gpio_path/gpio mode 6 out
$gpio_path/gpio mode 1 out

#left wheel
$gpio_path/gpio mode 4 out
$gpio_path/gpio mode 5 out
