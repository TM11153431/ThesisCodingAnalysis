window.onload = function(){
    main();
}

const folder = "Data";

function main(){
    d3.json(folder + "/processedData.json").then(function(codes){

        scaleColour = d3.scaleLinear()
            .domain([1, 25])
            .range(["#e5f5f9", "#2ca25f"])

        d3.selectAll("button")
            .data(Object.keys(codes))
            .enter().append("button")
            .attr("class", "button")
            .text(function(d){
                return d;
            })
            .style("background-color", function(d){
                if (d == "none"){
                    return "black";
                }
                return scaleColour(codes[d].count);
            })
            .on("click", function(d){
                codes[d].quotes.forEach(function(quote){
                    console.log(quote);
                })
                console.log("");
                console.log("");
                console.log("");
            });
    })
}
