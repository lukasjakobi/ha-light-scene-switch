# Light Scene Switch

![GitHub release (with filter)](https://img.shields.io/github/v/release/lukasjakobi/ha-light-scene-switch)
[![GitHub license](https://img.shields.io/github/license/lukasjakobi/ha-light-scene-switch)](https://github.com/lukasjakobi/ha-light-scene-switch/blob/master/LICENSE)

This repository contains a [Home Assistant](https://www.home-assistant.io/) [Python Script](https://www.home-assistant.io/integrations/python_script/) that enables text-to-speech (TTS) messaging across multiple media player entities. It offers features like caching, language selection and volume control (including automatically resetting the volume after the announcement to the previous state).

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=lukasjakobi&repository=ha-light-scene-switch&category=automations)

  ```yaml
  service: python_script.light_scene_switch
  data:
    scenes:
      - scene.scene_1
      - scene.scene_2
      - scene.scene_3
    id: "example"
  ```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

## Contact

Lukas Jakobi - lukas@jakobi.io

Project Link: [https://github.com/lukasjakobi/ha-sync-announcement](https://github.com/lukasjakobi/ha-sync-announcement)
