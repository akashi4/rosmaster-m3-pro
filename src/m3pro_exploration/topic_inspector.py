#!/usr/bin/env python3
"""Starter script to inspect active ROS2 topics on the ROSMASTER M3 Pro.

Run this on the robot (or on a machine sharing the same ROS_DOMAIN_ID)
after sourcing ROS2 Humble.
"""

import subprocess
import sys


KEY_PREFIXES = ("/odom", "/imu", "/scan", "/cmd_vel", "/camera", "/joint_states")


def list_topics() -> list[str]:
    """Return the list of currently active ROS2 topics."""
    result = subprocess.run(
        ["ros2", "topic", "list"],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        print(f"Erreur ros2 topic list: {result.stderr.strip()}", file=sys.stderr)
        return []
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def main() -> int:
    topics = list_topics()
    if not topics:
        print("Aucun topic ROS2 détecté (vérifiez le bringup ou ROS_DOMAIN_ID).")
        return 1

    print(f"Topics ROS2 détectés ({len(topics)}) :")
    for topic in topics:
        marker = "*" if topic.startswith(KEY_PREFIXES) else " "
        print(f"  {marker} {topic}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
