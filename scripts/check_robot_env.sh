#!/usr/bin/env bash
# Script de diagnostic rapide à exécuter sur le Jetson Orin NX 16 Go du ROSMASTER M3 Pro.
set -euo pipefail

echo "=== 1. Système & Mémoire ==="
uname -a
free -h

echo ""
echo "=== 2. Périphériques USB & Série ==="
lsusb || true
ls -l /dev/ttyUSB* /dev/ttyACM* /dev/video* 2>/dev/null || echo "Aucun périphérique /dev/ttyUSB*, /dev/ttyACM* ou /dev/video* détecté."

echo ""
echo "=== 3. Environnement ROS2 ==="
if command -v ros2 >/dev/null 2>&1; then
  echo "ROS_DISTRO=${ROS_DISTRO:-non défini}"
  echo "--- Nœuds actifs ---"
  ros2 node list || true
  echo "--- Topics actifs ---"
  ros2 topic list || true
else
  echo "ros2 introuvable dans le PATH (pensez à sourcer /opt/ros/humble/setup.bash)."
fi
