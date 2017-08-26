$(function() {
  $(".destroy").on("click", function(e) {
    e.preventDefault();
    if (window.confirm("本当に削除しますか？")) {
      var $this = $(this);
      var url = $this.data('url');
      var jqxhr = $.post(url, {
          csrfmiddlewaretoken: $("#csrf_token").val()
        })
        .done(function() {
          $this.closest('tr').fadeOut();
        })
        .fail(function() {
          alert("削除に失敗しました。");
        });
    };
  });
});
