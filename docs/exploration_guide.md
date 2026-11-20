# Guide d'Exploration et de Prise en Main — ROSMASTER M3 Pro (Jetson Orin NX 16 Go)

Ce guide rassemble les commandes et points d'entrée utiles pour explorer votre robot, inspecter les capteurs et démarrer le développement sur **Jetson Orin NX Super 16 Go** (Ubuntu + ROS2 Humble natif).

---

## 1. Connexion & Inspection Système (Jetson Orin NX 16 Go)

1. **Connexion SSH au robot :**
   ```bash
   ssh <utilisateur>@<ip-du-robot>
   ```
2. **Vérifier les ressources système, GPU et modes d'alimentation Jetson :**
   ```bash
   free -h                  # Doit afficher ~16 Go de RAM
   tegrastats               # Charge CPU / GPU / RAM / température en temps réel
   # Ou si jetson-stats est installé :
   jtop
   ```
3. **Vérifier les périphériques USB/Série connectés (STM32, LiDARs, caméra DABAI DCW2, audio) :**
   ```bash
   lsusb
   ls -l /dev/ttyUSB* /dev/ttyACM* /dev/video*
   ```

---

## 2. Récupérer le dépôt officiel Yahboom

Pour avoir les sources, fichiers URDF, configurations MoveIt et scripts de lancement localement dans votre espace de travail :

```bash
git clone https://github.com/YahboomTechnology/ROSMASTER-M3PRO.git
```

---

## 3. Inspection de l'environnement ROS2 Humble

Avant de lancer vos propres nœuds, vérifiez ce qui tourne déjà au démarrage (services systemd / micro-ROS agent) :

```bash
# Lister les nœuds et topics actifs
ros2 node list
ros2 topic list

# Vérifier les transformations TF (châssis, LiDARs, caméra, bras)
ros2 run tf2_tools view_frames
```

### Vérifier chaque capteur individuellement
- **Châssis / IMU / Odométrie (via pont micro-ROS STM32) :**
  Inspectez les topics publiés (`ros2 topic list | grep -E "imu|odom|vel"`) puis vérifiez la fréquence :
  ```bash
  ros2 topic hz /odom
  ```
- **Double LiDAR T-Mini Plus :**
  Vérifiez les scans laser (`ros2 topic list | grep scan`) et visualisez sous RViz2.
- **Caméra Orbbec DABAI DCW2 :**
  Vérifiez les topics RGB / Depth (`ros2 topic list | grep -E "camera|depth|color"`).

---

## 4. Commandes de Bringup & Tests de base

*(Les noms exacts des packages/launch files dépendent du workspace Yahboom installé sur votre Jetson ; vérifiez dans `~/yahboomcar_ws` ou le dépôt cloné.)*

1. **Démarrer le bringup matériel (châssis + capteurs de base) :**
   ```bash
   ros2 launch yahboomcar_bringup bringup.launch.py
   ```
2. **Téléopération clavier (dans un second terminal) :**
   ```bash
   ros2 run yahboomcar_ctrl yahboom_keyboard
   ```
3. **Lancer la stack SLAM / Navigation :**
   ```bash
   ros2 launch yahboomcar_nav laser_bringup_launch.py
   ```

---

## 5. Pistes d'exploration avancée (16 Go RAM)

Avec **16 Go de RAM unifiée** sur le Jetson Orin NX Super, vous disposez d'une marge confortable pour faire tourner simultanément :
- La stack **ROS2 Humble + Nav2 + MoveIt2** ;
- Des modèles de vision (**YOLO / VLM** quantifiés) sur les flux de la caméra **DABAI DCW2** ;
- Des LLM locaux légers / moyens (ex. via Ollama ou TensorRT-LLM) pour l'interaction vocale et la planification d'actions.
