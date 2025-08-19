package org.vimpiarte.store.basicBeans;

import org.springframework.context.annotation.Lazy;
import org.springframework.stereotype.Component;

/**
 * If an object is costly to create, we
 * can delay the creation of a bean until it's needed
 * <p>
 * Use the @Lazy annotation.
 */
@Component
@Lazy
public class HeavyResource {

    public HeavyResource() {
        System.out.println("Heavy Resource created");
    }
}
