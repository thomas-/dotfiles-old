# xinit

#xbindkeys
#xmodmap .Xmodmap
#hsetroot -full wallpaper.jpg
#exec i3
#

i3() {
		xbindkeys
		xmodmap .Xmodmap
		xrdb load .Xresources
		#./wall
		hsetroot -full wallpaper.jpg
		redshift -l 52.97:1.18 -t 6400:4800 &
		udiskie &
		exec i3
}


DEFAULT_SESSION=i3

case $1 in
	i3)
		i3
		;;
	dwm)
		xbindkeys
		xmodmap .Xmodmap
		hsetroot -full wallpaper.jpg
		while true; do
		   xsetroot -name "$( date +"%F %R" )"
		   sleep 1m    # Update time every minute
		done &
		exec dwm
		;;
	e17)
		xbindkeys
		xmodmap .Xmodmap
		exec enlightenment_start
		;;
	cinnamon)
		exec gnome-session-cinnamon
		;;
	lxde)
		xmodmap .Xmodmap
		exec startlxde
		;;
	*)
		i3
		;;
esac
