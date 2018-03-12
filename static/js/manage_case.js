
    function delete_case(){
        var caseid = $("button[name='dbtn']").attr("id");
        $.ajax({
            url:'/case_delete_data/',
            type:'POST',
            data:{"caseid":caseid},
            dataType:'JSON',

            success:function(data){
                alert("success_ajax");
            }

        });
    }