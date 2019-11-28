from tkinter import Canvas, Tk, mainloop, NW, Label, Frame, W

#parameters
width = 800
height = 800

nn_shape = [5, 2]

weights = [
    [
        [2, 3],
        [0.2, .1],
        [5, .1],
        [1, 1],
        [7, 2.1],
    ]
]

biases = [
    [
        30,
        -50
    ]
]

master = Tk()
canvas = Canvas(master, width=width, height=height, bg='#fff')


#functions

def calcLayersAxis(width, nn_shape, padding):
    #the avaliable space on the x axis
    avaliable_x = (width - (padding[1] + padding[3]))
    
    x_offset = int(avaliable_x/len(nn_shape))
    layers_axis_x = []
    for index, layer in enumerate(nn_shape, start=0):
        layers_axis_x.append((index*x_offset)+padding[3])
    return layers_axis_x
def calcNeuronsAxisY(height, nn_shape, padding):
    #the avaliable space on the y axis
    avaliable_y = (height - (padding[0] + padding[2]))
    max_n_neurons = max(nn_shape)
    y_offset = int(avaliable_y/max_n_neurons)
    neurons_axis_y = []
    for i in range(0, max_n_neurons+1):
        neurons_axis_y.append((y_offset*i)+padding[0])
    return neurons_axis_y
def calcNeuronsAxis(width, height, nn_shape, padding = [10, 10, 10, 10]):
    layers_axis_x = calcLayersAxis(width, nn_shape, padding)
    neurons_axis_y = calcNeuronsAxisY(height, nn_shape, padding)
    return {
        'layers': layers_axis_x,
        'neurons': neurons_axis_y
    }
def combineAxis(neurons_axis, nn_shape, neuron_size):
    layers_axis = neurons_axis['layers']
    neurons_axis_y = neurons_axis['neurons']

    axis = []
    for i, layer_size in enumerate(nn_shape):
        for j in range(0, layer_size):
            axis.append([layers_axis[i], 
                        neurons_axis_y[j], 
                        layers_axis[i]+neuron_size, 
                        neurons_axis_y[j]+neuron_size])
    return axis


    

    
    

def draw_nn(width, height, nn_shape, weights, biases, canvas, padding = [10, 10, 10, 10]):
    neuron_size = 30
    # padding [top right bottom left]
    neurons_axis = calcNeuronsAxis(width, height, nn_shape)
    combined_axis = combineAxis(neurons_axis=neurons_axis, nn_shape=nn_shape, neuron_size=neuron_size)
    for axis in combined_axis:
        canvas.create_oval(axis[0], axis[1], axis[2], axis[3], fill="#000")
draw_nn(width=width, height = height, nn_shape=nn_shape, weights = weights, biases = biases,
canvas = canvas)
canvas.pack()
mainloop()