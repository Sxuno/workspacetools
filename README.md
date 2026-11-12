# Version Update Notes C++

## Automation
### Build Selector  
compileproject.sh 

Console > GenerateProjectFiles  
Console > BuildProjectFiles  
Console > Exits  

## Build Version
update ProjectFileEditor.Target.cs

```cpp
	DefaultBuildSettings = BuildSettingsVersion.V6; // Version dependend
	IncludeOrderVersion = EngineIncludeOrderVersion.Unreal5_7; // Version
```
## Build Methods
generate project files 

```
~/Engine/Build/BatchFiles/Linux/GenerateProjectFiles.sh -project="PATHTOUPROJECTFILE"
```

build project file binaries

```sh
#!/bin/bash

# PROJECT STRUCTURE
# ~/PROJECT_NAME/                           PROJECT_NAME
# ~/PROJECT_NAME/source                     SOURCEDIR
# ~/PROJECT_NAME/source/PROJECT_NAME        UEPROJECTFILES

# path to engine
ENGINE_DIR="/UnrealEngine/Source/"

# detect Project name
SOURCE_DIR=$(dirname "$(realpath "$0")")
    IFS='/' read -ra FOLDERS <<< "$SOURCE_DIR"

PROJECT_NAME=${FOLDERS[-2]}
PROJECT_PROJECTFILES="$SOURCE_DIR/$PROJECT_NAME"

# run build script
"$ENGINE_DIR/Engine/Build/BatchFiles/Linux/Build.sh" "$PROJECT_NAME"Editor Linux Development -project="$PROJECT_PROJECTFILES/$PROJECT_NAME.uproject"

# wait for input
read -n 1
```

build plugin file binaries
```sh
#!/bin/bash

# PLUGIN STRUCTURE
# ~/PROJECT_NAME/source/PROJECT_NAME/Plugins					DIR_PLUGIN
# ~/PROJECT_NAME/source/PRJOECT_NAME/Plugins/PLUGIN_NAME		PLUGINFILES

PLUGIN_DIR="$PROJECT_FILES/Plugins"
# -------------------------------
# SCAN PLUGINS
# -------------------------------
mapfile -t PLUGIN_ARRAY < <(find "$PLUGIN_DIR" -mindepth 1 -maxdepth 1 -type d -exec basename {} \;)

if [$#PLUGIN_ARRAY[@] -eq 0]M then
	echo "No plugins found in $PLUGINS_DIR"
	exit 1
fi
# -------------------------------
# DISPLAY OPTIONS
# -------------------------------
echo "Availabel plugins:"
for i in "${!PLUGIN_ARRAY[@]}"; do
	echo " [$i] ${PLUGIN_ARRAY[$i]}"
done
# -------------------------------
# USER SELECTION
# -------------------------------
read -p "Select a plugin by name: " selection
if ! [[ "$selection" =~ ^[0-9]+$]] || ["$selection" -ge "${#PLUGIN_ARRAY[@]}"];then
	echo "Invalid selection"
	exit 1
fi

SELECTED_PLUGIN="${PLUGIN_ARRAY[$selection]}"
echo "You selected plugin: $SELECTED_PLUGIN"

# -------------------------------
# DO SOMETHING WITH SELECTED PLUGIN
# -------------------------------
# Example: just print the path
PLUGIN_PATH="$PLUGINS_DIR/$SELECTED_PLUGIN"
echo "Full path: $PLUGIN_PATH"
```
### notes
```
/Path/To/UnrealEngine/Engine/Binaries/DotNET/UnrealBuildTool/UnrealBuildTool.dll \
    -project="/media/stefan-wienold/UnrealEngine/Projects/IsekaiAdventures/source/IsekaiAdventures/IsekaiAdventures.uproject" \
    BlenderPointcloudsEditor Linux Development \
    -TargetType=Editor \
    -ModuleWithSuffix=BlenderPointclouds,3603
```