extends Control

@onready var TE_ExtractFrom = get_node("VBoxContainer/VSplitContainer/MarginContainer/VSplitContainer/VBoxContainer/HBoxContainer/Extract From/TE_Extract From")
@onready var TE_ExtractTo = get_node("VBoxContainer/VSplitContainer/MarginContainer/VSplitContainer/VBoxContainer/HBoxContainer/Extract To/TE_Extract To")
@onready var TE_NewFolderName = get_node("VBoxContainer/VSplitContainer/MarginContainer/VSplitContainer/VBoxContainer/HBoxContainer/Extract To2/TE_NFldName")
var CheckBoxStateDOZ = false

func _on_btn_run_pressed():
	var Errors = false
	if(TE_ExtractFrom.get_text() == ""):
		TE_ExtractFrom.set_placeholder("FILL")
		Errors = true
	if(TE_ExtractTo.get_text() == ""):
		TE_ExtractTo.set_placeholder("FILL")
		Errors = true
	if(!Errors):
		Global.RunPython(TE_ExtractFrom.get_text(), TE_ExtractTo.get_text(), TE_NewFolderName.get_text(), CheckBoxStateDOZ)

func _on_check_button_toggled(toggled_on):
	CheckBoxStateDOZ = toggled_on
