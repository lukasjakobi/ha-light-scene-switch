ACTION_MODE_LAST = "last"
ACTION_MODE_CURRENT = "current"
ACTION_MODE_NEXT = "next"

CURRENT_SCENE_ENTITY_ID_TEMPLATE = "sensor.light_szene_switch_{}"


def update_index(id: str, value: int):
    hass.states.set(CURRENT_SCENE_ENTITY_ID_TEMPLATE.format(id), value)


def get_index(id: str) -> int:
    index = hass.states.get(id)

    if index is None:
        update_index(id, 0)
        return 0

    return index


def activate_scene(scenes: list[str], index: int):
    if index >= len(scenes) or index < 0:
        return

    hass.services.call('scene', 'turn_on', {'entity_id': scenes[index]})


# the unique identifier for any light switch or similar
id = data.get('id') or None

# list of scene entities
scenes = data.get('scenes') or []

# the mode to use (last, next)
mode = data.get('mode') or None

if type(id) is not str:
    raise ValueError('"id" has to be provided')

if len(scenes) == 0:
    raise ValueError('"scenes" cannot be empty')

index = get_index(id)

if mode == ACTION_MODE_LAST:
    index -= 1
elif mode == ACTION_MODE_NEXT:
    index += 1

update_index(id, index)
activate_scene(scenes, index)
