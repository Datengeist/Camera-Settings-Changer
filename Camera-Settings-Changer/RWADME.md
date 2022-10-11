# Camera settings changer
## Wie man es nutzt
Bevor man das Script ausführen kann muss man noch ein bisschen was installieren
1. Natürlich muss [Python](https://www.python.org) und somit auch Pip installiert sein.
2. öffnet die Eingabeaufforderung oder die Konsole mit `Strg` + `Ö`
3. gebt dort pip install ` pip install opencv-python` ein um cv2 nutzen zu können
4. Passt den Code für euch euch an
    * zuerst wählt ihr eure Kamera aus in Zeile 4. 
        * 0 sollte schon passen, es sei den ihr habt mehrere Kameras, dann müsst ihr ausprobieren, welcher Indexplatz eure Kamera ist.
    * danach passt ihr unten die Werte an, dass funktioniert nur, wenn die Kamera diese eingabe werte auch unterstützt
    * sollte ein Wert bei mir nicht angepasst werden, der bei auch angepasst  werden muss, dann gebt ihr `capture.set(cv2.CAP_PROP_<Einstellung>, <Wert>)` ein. 
        * `<Einstellungen>` = Welche Einstellungen verfügbar sind könnt ihr euch durch das drücken von `Strg` + `Space` sehen nachdem ihr alles bis dahin eingefügt habt
        * `<Wert>` = hier gebt ihr den wert ein, den ihr braucht


## Warum ich es gemacht hab
Ich spiele gerne Switch spiele, wärend ich mich anderen Leuten in Discord rede. So kam es zu der Idee, dass ich es doch den Leuten über meine Capture Card streamen kann. Allerdings passen halt die Video-Einstellungen nicht und nach jedem PC neustart setzte es sich zurück. Also hab ich ein Script geschrieben, dass die Einstellungen, die ich brauche immer auf einen im Script festgelegten Wert stellt. Dieses Script hab ich dann in den Windows autostart Ordner gelegt, damit es bei jedem PC Neustart die Werte zurücksetzt

