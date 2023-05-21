function remove_children() {

    // 부모 노드 선택

    const parent = document.getElementById('parent');

   

    // 자식 노드 삭제

    while(parent.firstChild)  {

      parent.firstChild.remove()

    }

  }