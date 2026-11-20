# Yahboom ROSMASTER M3 Pro — Projet d'Exploration & Développement

Projet de référence et de démarrage pour explorer et développer sur le **Yahboom ROSMASTER M3 Pro**.

## Configuration de votre exemplaire

- **Carte contrôleur principale (SBC) :** NVIDIA Jetson Orin NX Super **16 Go** — environnement natif Ubuntu + ROS2 Humble
- **Contrôleur bas niveau :** STM32 (pont **micro-ROS**) + **IMU 9 axes** intégré
- **Châssis :** Alliage d'aluminium (`19,8 × 17,8 × 16,8 cm`), 4 roues **Mecanum 80 mm**, suspension arrière pendulaire
- **LiDAR :** Double LiDAR ToF **YDLIDAR T-Mini Plus** (avant-gauche & arrière-droite, 360°, 0,05–12 m)
- **Caméra de profondeur :** **Orbbec DABAI DCW2** (stéréo binoculaire à lumière structurée, jusqu'à 5 m)
- **Bras robotique :** Bras **6-DOF** à servomoteurs bus série (charge utile ~410 g, répétabilité ~0,5 mm, compatible MoveIt)
- **Écran & Audio :** Écran tactile **IPS HD 7 pouces** + module audio et reconnaissance vocale intégré
- **Batterie :** Pack **9 600 mAh** (chargeur DC 12,6 V / 2 A)

## Structure du projet

```text
rosmaster-m3-pro/
├── README.md
├── .gitignore
├── config/
│   └── robot_profile.yaml          # Profil matériel structuré de votre robot
├── docs/
│   ├── hardware_specs.md           # Fiche technique complète & variantes
│   ├── software_architecture.md    # Stack Ubuntu, ROS2 Humble, micro-ROS, MoveIt, IA
│   └── exploration_guide.md        # Guide SSH, diagnostics ROS2, bringup, SLAM
├── scripts/
│   └── check_robot_env.sh          # Script de diagnostic système & ROS2 sur le Jetson
└── src/
    └── m3pro_exploration/
        └── topic_inspector.py      # Script Python pour lister les topics clés ROS2
```

## Documentation détaillée

- [docs/hardware_specs.md](docs/hardware_specs.md) — Spécifications matérielles détaillées.
- [docs/software_architecture.md](docs/software_architecture.md) — Architecture logicielle ROS2 Humble, micro-ROS, MoveIt & IA.
- [docs/exploration_guide.md](docs/exploration_guide.md) — Guide pas-à-pas d'exploration et commandes de démarrage.
- [config/robot_profile.yaml](config/robot_profile.yaml) — Configuration matérielle au format YAML.

## Ressources officielles

- **Dépôt GitHub officiel :** https://github.com/YahboomTechnology/ROSMASTER-M3PRO
- **Portail de cours & documentation Yahboom :** https://www.yahboom.net/study/ROSMASTER-M3PRO
- **Support technique Yahboom :** support@yahboom.com
