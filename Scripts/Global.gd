extends Node

var DIR = OS.get_executable_path().get_base_dir()
var interpreterPath = DIR.path_join("Python/venv/Scripts/python.exe")
var scriptPath = DIR.path_join("Index.py")

func RunPython(FromLocation, ToLocation, NewFolderName, ToDelete):
	if !OS.has_feature("standalone"):
		interpreterPath = ProjectSettings.globalize_path("res://Python/venv/Scripts/python.exe")
		scriptPath = ProjectSettings.globalize_path("res://Index.py")
	OS.create_process("python", [scriptPath, FromLocation, ToLocation, NewFolderName, ToDelete], true)
