import AquariumEngineMorePipes

if __name__ == '__main__':
    app = AquariumEngineMorePipes.Aquarium(
        n_pipes=3,
    )
    app.game_loop()