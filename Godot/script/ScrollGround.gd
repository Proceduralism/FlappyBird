extends Node


# Declare member variables here. Examples:
# var a = 2
# var b = "text"


# Called when the node enters the scene tree for the first time.

export(float) var scroll_speed = 0.1

func _ready():
	self.material.set_shader_param("scroll_speed", scroll_speed)


# Called every frame. 'delta' is the elapsed time since the previous frame.

#func _process(delta):
#	pass
