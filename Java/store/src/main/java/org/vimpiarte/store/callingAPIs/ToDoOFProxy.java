package org.vimpiarte.store.callingAPIs;

import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.context.annotation.Primary;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

@Primary
@FeignClient(name = "todo", url = "${externalJson.service.url}")
public interface ToDoOFProxy extends ToDoProxy {

    @GetMapping("todos/{id}")
    ToDo getToDo(@PathVariable Integer id);
}
