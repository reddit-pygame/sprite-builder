#Build-A-Sprite

This challenge focuses on creating a tool to create and save sprite images for use in your games. The sprites are constructed from the 
sprite components created by opengameart user TokyoGeisha. The included code handles loading the images from the spritesheets or you
 are welcome to use your own implementation.


Challenge thread: https://www.reddit.com/r/pygame/comments/4g3m7n/challenge_buildasprite/

#Challenge

Create an app that allows the user to create a sprite image using the components found in the github repo (I combined the spritesheets from the different
 sprite sets, added recolored versions and reorganized the spritesheets to be more uniform). For each component (hair, eyes, tops, etc.), the user should
 be able to change the color and style as well as toggling whether that component is used at all. The user should also be able to save the sprites they create.
 
The image loading in the provided code creates a dict for each type of sprite component. Most components have different styles and colors and are stored in
 nested dicts ([color][style]) with integer keys. For example, TOPS[0][0] is a white shirt, TOPS[0][1] is a white v-neck shirt, TOPS[1][0] is a light gray shirt,
 TOPS[1][1] is a light gray v-neck. The integer for each color is the same for all components that have both color and style variants. Components like shoes
 and skin that only have one variation (color or style) are stored in flat dicts keyed by integer.

###Some Links

[Original sprite set](http://opengameart.org/content/pixel-people)

[Expansion Pack 1](http://opengameart.org/content/pixel-people-extras-01)

[Expansion Pack 2]( http://opengameart.org/content/pixel-people-extras-2)

[Reorganized Spritesheets](https://github.com/reddit-pygame/sprite-builder/tree/master/resources/graphics) - even if you're not using the provided code, it'll probably be easier to just download the whole repo

###Achievements

On Background - Allow the user to change the background/screen color

Accessorize, Accessorize - Add accessories like belts, necklaces, ties or whatever floats your boat  

*Good luck, have fun and feel free to ask for help if you need it*

#####Previous Challenges

[Draw Order Challenge](https://www.reddit.com/r/pygame/comments/3de4ng/challenge_drawing_in_the_right_order/) | 
[Spawn, Collide, Wrap](https://www.reddit.com/r/pygame/comments/3eddbp/challenge_spawn_collide_wrap/) | 
[Thruster Style Movement](https://www.reddit.com/r/pygame/comments/3fe60j/challenge_thruster_style_movement/) | 
[Conway User Interaction](https://www.reddit.com/r/pygame/comments/3iwdqq/challenge_conway_user_interaction/) |
[JSON Loading Challenge](https://www.reddit.com/r/pygame/comments/3lafr3/json_loading_challenge/) | 
[Map Distance Challenge](https://www.reddit.com/r/pygame/comments/3oc19d/map_distance_challenge/) | 
[Caching Pumpkins](https://www.reddit.com/r/pygame/comments/3qc9wm/challenge_caching_pumpkins/) | 
[A Puzzling World](https://www.reddit.com/r/pygame/comments/3s9m2j/challenge_a_puzzling_world/) | 
[Turkey Shoot](https://www.reddit.com/r/pygame/comments/3tvc5h/challenge_turkey_shoot/) | 
[All Downhill From Here](https://www.reddit.com/r/pygame/comments/3vsc5x/challenge_all_downhill_from_here/) | 
[Christmas Cannon](https://www.reddit.com/r/pygame/comments/3xpi6t/challenge_christmas_cannon/) | 
[Color Picker](https://www.reddit.com/r/pygame/comments/40mdi8/challenge_color_picker/) | 
[Minigolf Part I: Prototype](https://www.reddit.com/r/pygame/comments/4335cs/challenge_minigolf_part_1_prototype/) | 
[Skeet Shoot](https://www.reddit.com/r/pygame/comments/46xbxo/challenge_skeet_shoot/) | 
[Spin Class](https://www.reddit.com/r/pygame/comments/4aq3or/challenge_spin_class/) | 
[Egg Lob](https://www.reddit.com/r/pygame/comments/4dcvq4/challenge_egg_lob/)

