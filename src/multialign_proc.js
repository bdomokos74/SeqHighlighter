$( document ).ready(function() {
    console.log("len="+window.kmers.length);
    var cnt = 0

//    TODO read multiseq and create dom
    for(var nkmer=0; nkmer < window.kmers.length; nkmer++) {
        $("#kmers").append("<h3>num="+window.kmers[nkmer][0]+"</h3>")
        for(var k=1;k<window.kmers[nkmer].length; k++) {
            $("#kmers").append("<span class=\"kmer_pair\" id=\"kmer_"+cnt+
                "\"><span class=\"sel_seq\">"+window.kmers[nkmer][k][0]+
                "</span>/<span class=\"rev_seq\">"+window.kmers[nkmer][k][2]+
                "</span></span> ");
            function resetHighlight() {
                for( var i=0; i<window.seqlen; i++) {
                    $("#nuc_"+i).removeClass("sel_seq");
                    $("#nuc_"+i).removeClass("rev_seq");
                    $("#nuc_"+i).removeClass("mismatch_seq");
                    $("#nuc_"+i).removeClass("overlap_seq");
                }
            }
            function resetSelected() {
                $(".kmer_pair").removeClass("selected_item");
            }
            function otherClass(clss) {
                if( clss == "sel_seq") {
                    return("rev_seq");
                } else if( clss == "rev_seq") {
                    return("sel_seq");
                }
            }
            function highlightKmer(index, clss, kmerStr) {
                for(var i=0; i<window.kvalue; i++ ) {
                    var pos=index+i;
                    if( $("#nuc_"+pos).hasClass(otherClass(clss)) ||
                        $("#nuc_"+pos).hasClass(clss)) {
                        $("#nuc_"+pos).addClass("overlap_seq");
                    }
                    $("#nuc_"+pos).addClass(clss);
                    if( $("#nuc_"+pos).text() != kmerStr[i] ) {
                        $("#nuc_"+pos).addClass("mismatch_seq");
                    }
                }
            }
            function bindHighlightFun(n, k, cnt) {
                $("#kmer_"+cnt).click(function() {
                    resetSelected();
                    $("#kmer_"+cnt).toggleClass("selected_item");
                    resetHighlight();
                    for( var j=0; j<window.kmers[n][k][1].length; j++) {
                        var index = window.kmers[n][k][1][j];
                        highlightKmer(index, "sel_seq", window.kmers[n][k][0])
                    }
                    for( var j=0; j<window.kmers[n][k][3].length; j++) {
                        var index = window.kmers[n][k][3][j];
                        highlightKmer(index, "rev_seq", window.kmers[n][k][2]);
                    }
                });
            }
            bindHighlightFun(nkmer, k, cnt);
            cnt += 1;
        }

    }

});
