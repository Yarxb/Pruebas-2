default opciones = []

init python:
    nu = 0
    def a_C(kind):
        global opciones
        opciones = [
            {"label": "sum", "titulo": _("Hacer una suma"), "kind": "inicio"},
            
        ]
        if nu >= 1:
            opciones.append({"label": "date", "titulo": _("Invitarla a salir."), "kind": "inicio"})



screen opcions(adj):
    frame:

        xalign 0.7
        xsize 640
        ysize 400
        yalign 0.5

        has side "c r b"

        viewport:
            yadjustment adj
            mousewheel True
            draggable True

            vbox:
                for opcion in opciones:
                    if isinstance(opcion, dict) and opcion.get("kind") == "inicio":
                        textbutton opcion["titulo"]:
                            action Return(opcion)
                            left_padding 20
                            xfill True
                    elif isinstance(opcion, dict):
                        null height 10
                        text opcion.get("titulo", "") alt ""
                        null height 5

        bar adjustment adj style "vscrollbar"
        textbutton _("Es todo por ahora."):
            xfill True
            action Return(False)
            top_margin 10

default tutorials_adjustment = ui.adjustment()
default tutorials_first_time = True

###

label start:


    python:
        a_C("inicio")

    while True:

        call screen opcions(adj = tutorials_adjustment)

        $ operacion = _return

        if not operacion:
            jump end

        call expression operacion["label"] from _call_expression


label sum:

    $ n1 = float(renpy.input("Escribe el primer númerop qu quieres sumar: "))
    $ n2 = float(renpy.input("Ecribe el segundo número que quieres sumar: "))

    "El resultado de tu suma es [n1+n2]"
    return 