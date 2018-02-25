function bubblesort(input) {
    var n = input.length;
    var list = input.slice(); //copy the original array
    var index = [];
    for(i = 0; i < n; i++) {
       index.push(i);
    }
    
    var swap = true;
    while(swap) {
        swap = false;
        for(i = 1; i < n; i++) {
            if(list[i-1] < list[i]) {
                // swap list elements
                var t = list[i-1];
                list[i-1] = list[i];
                list[i] = t;
                // swap index
                var s = index[i-1];
                index[i-1] = index[i];
                index[i] = s;
                swap = true;
            }
        }
        n--;
    }
    
    return [list,index];
}
