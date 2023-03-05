import tcod

from engine import Engine
from entity import Entity
from Gmap import GameMap
from input_hande import EventHandler

def main() -> None:
    screen_wid = 90
    screen_hei = 60

    map_width = 90
    map_height = 60
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = Entity(int(screen_wid / 2), int(screen_hei / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_wid / 2 - 5), int(screen_hei / 2), "@", (255, 255, 0))
    entities = {npc, player}

    game_map = GameMap(map_width, map_height)
    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)
    with tcod.context.new_terminal(
        screen_wid,
        screen_hei,
        tileset=tileset,
        title="ProtoRED",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_wid, screen_hei, order="F")
        while True:
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()

            engine.handle_events(events)

if __name__ == "__main__":
    main()